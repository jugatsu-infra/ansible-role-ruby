import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# test if packages are installed
@pytest.mark.parametrize('name', [
    'build-essential',
    'ruby-full',
    'ruby-dev',
])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed


# test if bundler is installed
def test_bundler_is_installed(Command):
    cmd = Command('gem list -i bundler')
    assert cmd.stdout.rstrip() == 'true'
