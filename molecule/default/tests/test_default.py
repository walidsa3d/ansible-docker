def test_docker_is_installed(host):
    docker = host.package("docker-ce")
    assert docker.is_installed

def test_docker_running_and_enabled(host):
    docker = host.service("docker")
    assert docker.is_running
    #assert docker.is_enabled