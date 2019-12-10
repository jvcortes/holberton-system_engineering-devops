# Edits ~/.ssh/config to refuse to authenticate to a server by its password
include stdlib

file_line { 'Turn off passwd auth':
  path =>    '/etc/ssh/ssh_config',
  line =>    'PasswordAuthentication no'
}

file_line { 'Declare identity file':
  path =>    '/etc/ssh/ssh_config',
  line =>    'IdentityFile ~/.ssh/holberton'
}