# jenkins-ansible

This is used to provision Jenkins master & slave, each in docker and able to provision docker containers.  Also configures Jenkins Job builder for complete IaC deployment. 

This project is designed to operate using [clusterverse](https://github.com/dseeley/clusterverse) to manage the base infrastructure.  Please see the [README.md](https://github.com/dseeley/clusterverse/blob/master/README.md) there for instructions on deployment. 

## Configuration
Default configuration is stored in `roles/jenkins/_common/defaults/main.yml`.  Override in the `cluster_defs/**/app_vars.yml` files.

### Playbook execution
`cluster.yml` is included that is compatible with [clusterverse](https://github.com/dseeley/clusterverse). 

`redeploy.yml` is included that functions only in conjunction with [clusterverse](https://github.com/dseeley/clusterverse).


#### Invocation
```
ansible-playbook  -e cloud_type=esxifree -e clusterid=jenkins -e region=dougalab -e buildenv=tools cluster.yml
```
