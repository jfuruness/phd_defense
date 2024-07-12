from multiprocessing import cpu_count
from pathlib import Path
import time

from bgpy.simulation_engine import ROV, ROVPPV1Lite
from bgpy.enums import SpecialPercentAdoptions  # noqa
from bgpy.simulation_framework import (
    Simulation,
    SubprefixHijack,
    ScenarioConfig,
)


def main():

    sim = Simulation(
        percent_adoptions=(
            # SpecialPercentAdoptions.ONLY_ONE,
            0.01,
            0.1,
            0.2,
            0.5,
            0.8,
            0.99,
        ),
        scenario_configs=(
            ScenarioConfig(ScenarioCls=SubprefixHijack, AdoptPolicyCls=ROV),
            ScenarioConfig(ScenarioCls=SubprefixHijack, AdoptPolicyCls=ROVPPV1Lite),
        ),
        output_dir=Path("~/Desktop/phd_defense").expanduser(),
        num_trials=100,
        parse_cpus=cpu_count() - 2,
    )
    sim.run()


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    print(f"{time.perf_counter() - start}s")
