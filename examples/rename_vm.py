from ovirt_python_sdk import Ovirt

api = Ovirt(url='http://site.ru', username='username', password='password', ca_file='path_to_ca_file')

# Получаем ВМ
vm = api.get_vm_by_name('vm_name')

api.rename_vm(vm, 'new_vm_name')
