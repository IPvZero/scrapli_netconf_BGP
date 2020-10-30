"""
AUTHOR: IPvZero
Date: 29th Oct 2020
Purpose: Deploy iBGP over OSPF using NETCONF
"""

from nornir import InitNornir
from nornir_scrapli.tasks import netconf_edit_config
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.data import load_yaml
from nornir_jinja2.plugins.tasks import template_file

nr = InitNornir(config_file="config.yaml")


def load_vars(task):
    """
    Load host variables and bind them to a per-host dict key called "facts"
    """

    data = task.run(task=load_yaml, file=f"./host_vars/{task.host}.yaml")
    task.host["facts"] = data.result
    config_routing(task)


def config_routing(task):
    """
    Build Routing template based on IOS-XE YANG Model
    Push configuration over NETCONF
    """

    routing_template = task.run(
        task=template_file,
        name="Buildling Routing Configuration",
        template="route.j2",
        path="./templates",
    )
    routing_output = routing_template.result
    task.run(task=netconf_edit_config, target="running", config=routing_output)


result = nr.run(task=load_vars)
print_result(result)
