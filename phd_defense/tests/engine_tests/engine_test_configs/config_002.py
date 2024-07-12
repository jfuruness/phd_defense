from frozendict import frozendict
from bgpy.tests.engine_tests.utils import EngineTestConfig

from bgpy.enums import ASNs

from bgpy.simulation_engine import BGP, ROV
from bgpy.simulation_framework import (
    ScenarioConfig,
    PrefixHijack,
)

from .as_graph_info import as_graph_info


desc = "Prefix Hijack against BGP"

config_002 = EngineTestConfig(
    name="config_002",
    desc=desc,
    scenario_config=ScenarioConfig(
        ScenarioCls=PrefixHijack,
        BasePolicyCls=BGP,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict(
            {
                ASNs.VICTIM.value: ROV,
            }
        ),
    ),
    as_graph_info=as_graph_info,
)
