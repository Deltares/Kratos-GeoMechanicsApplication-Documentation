import atexit
import sys
from pathlib import Path

import KratosMultiphysics.GeoMechanicsApplication as GeoMechanicsApplication


def _clean_up_geo_flow_instance(instance):
    del instance


def _main():
    # Additional analysis parameters
    working_dir = "."
    analysis_filename = "piping_analysis.json"
    critical_head_boundary_model_part_name = "PorousDomain.CriticalHeadBoundary"
    min_critical_head = 0.6
    max_critical_head = 1.3
    step_critical_head = 0.1

    try:
        geo_flow = GeoMechanicsApplication.CustomWorkflowFactory.CreateKratosGeoFlow()
        atexit.register(_clean_up_geo_flow_instance, geo_flow)

        critical_head_info = GeoMechanicsApplication.KratosExecuteCriticalHeadInfo(
            min_critical_head, max_critical_head, step_critical_head
        )

        logging = lambda msg: print(msg)
        no_progress_reporting = lambda fraction_done: None
        no_progress_message = lambda msg: None
        do_not_cancel = lambda: False
        callbacks = GeoMechanicsApplication.KratosExecuteCallBackFunctions(
            logging, no_progress_reporting, no_progress_message, do_not_cancel
        )

        return geo_flow.ExecuteFlowAnalysis(
            working_dir,
            analysis_filename,
            critical_head_info,
            critical_head_boundary_model_part_name,
            callbacks,
        )
    except Exception as e:
        print(f"Analysis ERROR: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(_main())
