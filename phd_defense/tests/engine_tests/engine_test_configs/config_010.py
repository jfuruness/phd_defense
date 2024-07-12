from frozendict import frozendict
from bgpy.tests.engine_tests.utils import EngineTestConfig

from bgpy.enums import ASNs

from bgpy.simulation_engine import BGP, ROV, ASPA
from bgpy.simulation_framework import (
    ScenarioConfig,
    PrefixHijack,
    preprocess_anns_funcs,
)

from .as_graph_info import as_graph_info


desc = "Shortest-Path Export-All Hijack against ASPA"

config_010 = EngineTestConfig(
    name="config_010",
    desc=desc,
    scenario_config=ScenarioConfig(
        ScenarioCls=PrefixHijack,
        BasePolicyCls=BGP,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict(
            {
                1: ASPA,
                2: ASPA,
                4: ASPA,
                10: ASPA,
                ASNs.VICTIM.value: ASPA,
            }
        ),
        preprocess_anns_func=preprocess_anns_funcs.shortest_path_export_all_hijack,
    ),
    as_graph_info=as_graph_info,
)
