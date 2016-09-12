from django.db import models
from django.contrib.auth.models import User
from Crypto.PublicKey import RSA


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import auth
from rest_framework.authtoken.models import Token
import uuid
from settings import Settings
from common_dibbs.misc import configure_basic_authentication

# Create your models here.


def generate_uuid():
    return uuid.uuid4()


class Credential(models.Model):
    site_name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='credentials', on_delete=models.CASCADE)
    credentials = models.TextField()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True,
                                related_name='profile')
    rsa_key = models.TextField(max_length=1024, blank=True, default='')


class Cluster(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    uuid = models.CharField(max_length=100, blank=False, default=generate_uuid)
    private_key = models.TextField(max_length=1000, blank=True, default='')
    public_key = models.TextField(max_length=1000, blank=True, default='')

    status = models.CharField(max_length=100, blank=True, default='IDLE')

    # Relationships
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='clusters', on_delete=models.CASCADE)
    appliance = models.CharField(max_length=100)
    appliance_impl = models.CharField(max_length=100, blank=True)
    common_appliance_impl = models.CharField(max_length=100, blank=True)

    def get_master_node(self):
        candidates = Host.objects.filter(cluster_id=self.id).filter(is_master=True)
        return candidates[0] if len(candidates) > 0 else None

    def get_full_credentials(self):
        from common_dibbs.clients.ar_client.apis.appliance_implementations_api import ApplianceImplementationsApi
        from common_dibbs.clients.ar_client.apis.sites_api import SitesApi
        import crypto

        # Create a client for ApplianceImplementations
        appliance_implementations_client = ApplianceImplementationsApi()
        appliance_implementations_client.api_client.host = "%s" % (Settings().appliance_registry_url,)
        configure_basic_authentication(appliance_implementations_client, "admin", "pass")

        # Create a client for Sites
        sites_client = SitesApi()
        sites_client.api_client.host = "%s" % (Settings().appliance_registry_url,)
        configure_basic_authentication(sites_client, "admin", "pass")

        appl_impl = appliance_implementations_client.appliances_impl_name_get(name=str(self.appliance_impl))

        user = auth.get_user_model().objects.get(id=self.user_id)
        full_credentials = None
        for creds in user.credentials.all():
            if creds.site_name == appl_impl.site:
                full_credentials = {
                    "site": sites_client.sites_name_get(name=creds.site_name),
                    "user": self.user,
                    "credentials": crypto.decrypt_credentials(creds.credentials, user_id=self.user_id)
                }
                break
        return full_credentials

    # def user(self):


class Host(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    is_master = models.BooleanField(default=False)
    instance_id = models.CharField(max_length=100, blank=True, default='')
    instance_ip = models.CharField(max_length=100, blank=True, default='')

    # Relationships
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)


# Add a token upon user creation
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Add a profile upon user creation
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(user=instance, rsa_key=RSA.generate(1024).exportKey())
