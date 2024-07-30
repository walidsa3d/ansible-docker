import os

def test_docker_installed(host):
    pkg = host.package("docker-ce")
    assert pkg.is_installed

def test_docker_service_is_enabled(host):
    service = host.service("docker")
    assert service.is_enabled

