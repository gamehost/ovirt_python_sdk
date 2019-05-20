from ovirt_python_sdk import Ovirt

api = Ovirt(url='http://site.ru', username='username', password='password', ca_file='path_to_ca_file')

# Создаем ВМ передавая необходимые параметры
vm = api.create_vm(name='vm_name', host=api.get_host_by_name('host_name'), memory=2**30, cpu_sockets=1)

# Удаляем ВМ
api.remove_vm(vm)
