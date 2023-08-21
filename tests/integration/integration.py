import pytest

# from neon_phal_plugin_audio_receiver.utils import auto_pair_bluetooth, auto_pair_kdeconnect
# from neon_phal_plugin_audio_receiver.utils import set_raspotify_device_name
# from neon_phal_plugin_audio_receiver.utils import set_uxplay_device_name
from neon_phal_plugin_audio_receiver.utils import interact_with_service, get_service_status

# auto_pair_bluetooth()
# auto_pair_kdeconnect()
# set_raspotify_device_name("Neon Mark 2")
# set_uxplay_device_name("Neon Mark 2")


@pytest.mark.xfail
def test_service_enable():
    # - Get the status of any of these services on the Mark 2
    services = ("uxplay", "raspotify", "bluetooth", "kdeconnect")
    for service in services:
        print(f"{service} is running? {get_service_status(service)}")

    # - Enable/disable the services
    for service in services:
        # You should see "True" for all of these messages
        interact_with_service(service, "stop")
        print(f"{service} stopped, did it register? {not get_service_status(service)}")
        interact_with_service(service, "start")
        print(f"{service} started, did it register? {get_service_status(service)}")
