import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("127.0.0.1", port=22, username='Prasad', password='password')

stdin, stdout, stderr = ssh.exec_command("command")
print(stdout.readlines())

channel = ssh.invoke_shell()
channel.send()
channel.recv_ready()
channel.recv(4096)