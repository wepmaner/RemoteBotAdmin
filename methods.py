import re
import subprocess
import logging

logger = logging.getLogger('methods')

# Детальная информация о сервисе
def service_cmd(action,name):
    cmd = cmd = f'systemctl {action} {name}' 
    try:
        result = subprocess.check_output(cmd,text=True,shell=True)
    except subprocess.CalledProcessError as e:
        result = e.output
    return result

# Краткая информация о сервисе
def get_status_low(name:str) -> str:
    result = service_cmd('status',name)
    name = re.findall('\*(?:\s\S+)+',result)[0]
    isactive = re.findall('Active:\s\S*\s\S*',result)[0]
    if 'active (running)' in isactive:
        active_text = '🟢 Работает'
    elif 'inactive (dead)' in isactive:
         active_text = '☠️ Не активен'
    elif 'failed' in isactive:
         active_text = '🔴 Ошибка'
    else:
        active_text = f'Статус неизвестен ({isactive})'
    
    memory = re.findall('Memory:\s\S*',result)
    if memory:
        memory = memory[0].split(' ')[1]
        memory_txt = f'💾 Память: {memory}'
    else:
        memory_txt = ''
    text = f'{name}\n\n{active_text}\n{memory_txt}'
    return text

def get_status_low(name:str) -> str:
    result = service_cmd('status', name)
    name_match = re.search('\*(?:\s\S+)+', result)
    name = name_match.group() if name_match else ''
    
    active_match = re.search('Active:\s(\S+)\s\((\S+)\)', result)
    if active_match:
        state = active_match.group(1)
        if state == 'active':
            active_text = '🟢 Работает'
        elif state == 'inactive':
            active_text = '☠️ Не активен'
        else:
            active_text = '🔴 Ошибка'
    else:
        active_text = f'Статус неизвестен ({result})'

    memory_match = re.search('Memory:\s(\S+)', result)
    memory_txt = f'💾 Память: {memory_match.group(1)}' if memory_match else ''

    return f'{name}\n\n{active_text}\n{memory_txt}'

