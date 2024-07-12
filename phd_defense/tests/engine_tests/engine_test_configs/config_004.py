from frozendict import frozendict
from bgpy.tests.engine_tests.utils import EngineTestConfig

from bgpy.enums import ASNs

from bgpy.simulation_engine import BGP, ROVPPV1Lite
from bgpy.simulation_framework import (
    ScenarioConfig,
    SubprefixHijack,
)

from .as_graph_info import as_graph_info


desc = "Subprefix Hijack against ROV++"

config_004 = EngineTestConfig(
    name="config_004",
    desc=desc,
    scenario_config=ScenarioConfig(
        ScenarioCls=SubprefixHijack,
        BasePolicyCls=BGP,
        override_attacker_asns=frozenset({ASNs.ATTACKER.value}),
        override_victim_asns=frozenset({ASNs.VICTIM.value}),
        override_non_default_asn_cls_dict=frozendict(
            {
                8: ROVPPV1Lite,
                9: ROVPPV1Lite,
                ASNs.VICTIM.value: ROVPPV1Lite,
            }
        ),
    ),
    as_graph_info=as_graph_info,
)
