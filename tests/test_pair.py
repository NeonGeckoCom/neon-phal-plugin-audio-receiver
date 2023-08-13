# pylint: disable=missing-function-docstring
from subprocess import CalledProcessError
from unittest.mock import call, patch, Mock

import pytest

from neon_phal_plugin_audio_receiver.utils import (
    auto_pair_bluetooth,
    auto_pair_kdeconnect,
)


def test_auto_pair_bluetooth():
    with patch("subprocess.run", return_value=Mock(returncode=0)) as mock_run:
        auto_pair_bluetooth()
    mock_run.assert_called_with("/usr/local/bin/autopair-bluetooth.sh 60", check=True)


def test_auto_pair_bluetooth_exception():
    with patch("subprocess.run", side_effect=CalledProcessError(1, "/usr/local/bin/autopair-bluetooth.sh 60")):
        with pytest.raises(CalledProcessError):
            auto_pair_bluetooth()


def test_auto_pair_kdeconnect():
    with patch("subprocess.run", return_value=Mock(returncode=0)) as mock_run, patch("time.sleep", return_value=None):
        auto_pair_kdeconnect()
    mock_run.assert_has_calls(
        [
            call("sudo /usr/local/bin/autopair-kdeconnect.sh 30", check=True),
        ]
    )


def test_auto_pair_kdeconnect_exception():
    with patch(
        "subprocess.run", side_effect=CalledProcessError(1, "sudo /usr/local/bin/autopair-kdeconnect.sh 30")
    ), patch("time.sleep", return_value=None):
        with pytest.raises(CalledProcessError):
            auto_pair_kdeconnect()
