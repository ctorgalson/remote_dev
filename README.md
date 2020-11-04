# Ansible Collection - ctorgalson.remote_dev

![Molecule Test](https://github.com/ctorgalson/remote_dev/workflows/Molecule%20Test/badge.svg)

An [Ansible collection](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)
designed for setting up remote web-dev workstations.

## Scenarios

### Docksal/mosh/vim/public

At present, the collection demonstrates one scenario: configuring a remote
development server based on my current day-to-day development needs, configured
as follows:

  - [Docksal](https://docksal.io/) as a development LAMP environment,
  - [mosh](https://mosh.org/) for stable roaming ssh connection,
  - [vim](https://github.com/vim/vim): for editing code directly on the remote server,
  - [clamav](https://www.clamav.net): for automated antivirus scanning,
  - [iptables](https://www.netfilter.org/projects/iptables/index.html): for firewalling the server,
  - [glances](https://nicolargo.github.io/glances): for a nice, command-line system monitor.

The default server configuration is fully firewalled execpt for ports for:

  - `http`,
  - `https`,
  - `mosh`,
  - `ntp`,
  - `ssh`.

When run, the scenario's playbook will create a connection script that starts
one of `ssh` or `mosh` with the right credentials and connection information.

## Using the collection

- [Install](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html#id2) the [collection](https://galaxy.ansible.com/ctorgalson/remote_dev).
  **Note**: installing the collection via `ansible-galaxy` hasn't been tested,
            and I can't guarantee yet that it works. If it doesn't, the
            collection will have to be installed manually.
- Create a new Ansible project including an [inventory file](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html),
- Copy the playbook for the scenario that most closely matches your use case
  from the collection's `playbooks/` directory into your project,
- Copy the `playbooks/group_vars/` files for the scenario matching the playbook
  into your projects' `group_vars/all/` directory,
- Customize the tasks in the playbook to suit your use case,
- Customize the variables files in `group_vars/all/` to suit your use case,
- Run the playbooks to provision your server,
- Connect to your newly-provisioned server with the auto-generated connection
  script.

This will look approximately like this:

```
ansible-galaxy collection install ctorgalson.remote_dev --pre
mkdir ~/myproject
cd ~/myproject
touch hosts.yml
# (Customize hosts.yml inventory file)
copy -R ~/.ansible/collections/ansible_collections/ctorgalson/remote_dev/playbooks/demo__docksal_mosh_vim_public.yml provision.yml .
mkdir -p group_vars/all
cp -R ~/.ansible/collections/ansible_collections/ctorgalson/remote_dev/playbooks/group_vars/docksal_mosh_vim_public/* ./group_vars/all/
# (Customize playbook)
# (Customize group_vars/all/*.yml)
ansible-playbook -i inventory.yml provision.yml
./redev.sh
```

## Roles

The collection uses numerous roles as submodules. Where possible, I've used my
own, but most of them are widely-used roles published in the Ansible community.
In alphabetical order by namespace/role-name, the collection's roles are:

- [`anarcher.volume` (`ansible-volume`)](https://galaxy.ansible.com/anarcher/volume)
- [`ctorgalson.apt` (`ansible-role-apt`)](https://galaxy.ansible.com/ctorgalson/apt)
- [`ctorgalson.docksal` (`ansible-role-docksal`)](https://galaxy.ansible.com/ctorgalson/docksal)
- [`ctorgalson.dotfiles` (`ansible-role-dotfiles`)](https://galaxy.ansible.com/ctorgalson/dotfiles)
- [`ctorgalson.files` (`ansible-role-files`)](https://galaxy.ansible.com/ctorgalson/files)
- [`ctorgalson.nvm` (`ansible-role-nvm`)](https://galaxy.ansible.com/ctorgalson/nvm)
- [`ctorgalson.oh-my-zsh` (`ansible-role-oh-my-zsh`)](https://galaxy.ansible.com/ctorgalson/oh-my-zsh)
- [`ctorgalson.nerdfonts` (`ansible-role-nerdfonts`)](https://galaxy.ansible.com/ctorgalson/nerdfonts)
- [`ctorgalson.platform` (`ansible-role-platform`)](https://galaxy.ansible.com/ctorgalson/platform)
- [`ctorgalson.ssh-keys` (`ansible-role-ssh-keys`)](https://galaxy.ansible.com/ctorgalson/ssh-keys)
- [`ctorgalson.vim` (`ansible-role-vim`)](https://galaxy.ansible.com/ctorgalson/vim)
- [`geerlingguy.clamav` (`ansible-role-clamav`)](https://galaxy.ansible.com/geerlingguy/clamav)
- [`geerlingguy.composer` (`ansible-role-composer`)](https://galaxy.ansible.com/geerlingguy/composer)
- [`geerlingguy.docker` (`ansible-role-docker`)](https://galaxy.ansible.com/geerlingguy/docker)
- [`geerlingguy.firewall` (`ansible-role-firewall`)](https://galaxy.ansible.com/geerlingguy/firewall)
- [`geerlingguy.nodejs` (`ansible-role-nodejs`)](https://galaxy.ansible.com/geerlingguy/nodejs)
- [`geerlingguy.php` (`ansible-role-php`)](https://galaxy.ansible.com/geerlingguy/php)
- [`geerlingguy.pip` (`ansible-role-pip`)](https://galaxy.ansible.com/geerlingguy/pip)
- [`geerlingguy.security` (`ansible-role-security`)](https://galaxy.ansible.com/geerlingguy/security)
- [`jnv.unattended-upgrades` (`ansible-role-unattended-upgrades`)](https://galaxy.ansible.com/jnv/unattended-upgrades)
- [`ocha.yarn` (`ansible-role-yarn`)](https://galaxy.ansible.com/ocha/yarn)
- [`weareinteractive.environment` (`ansible-environment`)](https://galaxy.ansible.com/weareinteractive/environment) 
- [`weareinteractive.users` (`ansible-users`)](https://galaxy.ansible.com/weareinteractive/users) 
- [`yatesr.timezone` (`ansible-timezone`)](https://galaxy.ansible.com/yatesr/timezone)
