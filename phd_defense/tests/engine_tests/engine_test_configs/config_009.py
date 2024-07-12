from frozendict import frozendict
from bgpy.tests.engine_tests.utils import EngineTestConfig

from bgpy.enums import ASNs

from bgpy.simulation_engine import BGP, ROV
from bgpy.simulation_framework import (
    ScenarioConfig,
    PrefixHijack,
    preprocess_anns_funcs,
)

from .as_graph_info import as_graph_info
from .edge_filter import EdgeFilter  # copy pasted from ASPA work


desc = "Forged-Origin Hijack against EdgeFilter"

config_009 = EngineTestConfig(
    name="config_009",
    desc=desc,
    scenario_config=ScenarioConfig(
        ScenarioCls=PrefixHijack,
        BasePolicyCls=BGP,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict(
            {
                1: EdgeFilter,
                ASNs.VICTIM.value: BGP,
            }
        ),
        preprocess_anns_func=preprocess_anns_funcs.forged_origin_export_all_hijack,
    ),
    as_graph_info=as_graph_info,
)
