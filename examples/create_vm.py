from time import sleep

from ovirtsdk4.types import VmStatus, DiskStatus

from ovirt_python_sdk import Ovirt

api = Ovirt(url='http://site.ru', username='username', password='password', ca_file='path_to_ca_file')
# Создаем ВМ передавая необходимые параметры
vm = api.create_vm(name='vm_name', host=api.get_host_by_name('shost1'), memory=2 ** 30, cpu_sockets=1)

# Проверяем что вм готова
while api.get_vm_status_by_name('vm_name') == VmStatus.IMAGE_LOCKED:
    sleep(1)

# Создаем и добавляем диск в ВМ
disk = api.create_vm_disk(
    vm=vm,
    storage_domain=api.get_storage_domain_by_name('Host1'),
    name='disk_name',
    description='disk_description',
    size=2 ** 30
)

# Ждем пока будет готов диск
while api.get_disk_by_name('disk_name').status != DiskStatus.OK:
    sleep(1)

api.start_vm(vm)

# Ждем запуск вм
while api.get_vm_status_by_name('vm_name') == VmStatus.UP:
    sleep(1)

api.stop_vm(vm)
# Ждем полную остановку
while api.get_vm_status_by_name('vm_name') == VmStatus.DOWN:
    sleep(1)

# Удаляем ВМ
api.remove_vm(vm)
