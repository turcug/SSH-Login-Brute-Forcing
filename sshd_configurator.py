import subprocess

def file_length():
    filename = 'top_100_passwords.txt'
    with open(filename, 'r') as f:
         num_lines = sum(1 for line in f)
    return num_lines

def SSH_Configurator(): 
    path = '/etc/ssh/sshd_config'
    val = 'MaxStartups {}\n'.format(file_length())

    with open(path, 'r') as f:
        sshd_config = f.readlines()

    max_startups_index = -1
    for i, line in enumerate(sshd_config):
        if line.startswith('MaxStartups'):
            max_startups_index = i
            break

    if max_startups_index != -1:
        sshd_config[max_startups_index] = val
    
    else:
        sshd_config.append(val)

    with open(path, 'w') as f:
        f.writelines(sshd_config)

    subprocess.run(['systemctl', 'restart', 'ssh'])
