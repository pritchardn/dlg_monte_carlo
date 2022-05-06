"""
dlg_monte_carlo appComponent module.

This is the module of dlg_monte_carlo containing DALiuGE application components.
Here you put your main application classes and objects.

Typically a component project will contain multiple components and will
then result in a single EAGLE palette.

Be creative! do whatever you need to do!
"""
import logging
import pickle
import random
import math

from dlg.drop import BarrierAppDROP, BranchAppDrop
from dlg.meta import (
    dlg_batch_input,
    dlg_batch_output,
    dlg_bool_param,
    dlg_component,
    dlg_float_param,
    dlg_int_param,
    dlg_streaming_input,
    dlg_string_param,
)

logger = logging.getLogger(__name__)

##
# @brief MyApp
# @details Template app for demonstration only!
# Replace the documentation with whatever you want/need to show in the DALiuGE
# workflow editor. The appclass parameter should contain the relative Pythonpath
# to import MyApp.
#
# @par EAGLE_START
# @param category PythonApp
# @param[in] param/appclass Application Class/dlg_monte_carlo.MyApp/String/readonly/
#     \~English Import direction for application class
# @param[in] param/dummy Dummy parameter/ /String/readwrite/
#     \~English Dummy modifyable parameter
# @param[in] port/dummy Dummy in/float/
#     \~English Dummy input port
# @param[out] port/dummy Dummy out/float/
#     \~English Dummy output port
# @par EAGLE_END

# Application components can inherit from BarrierAppDROP or BranchAppDrop.
# It is also possible to inherit directly from the AbstractDROP class. Please
# refer to the Developer Guide for more information.


class MonteCarloDROP(BarrierAppDROP):
    """A template BarrierAppDrop that doesn't do anything at all
    Add your functionality in the run method and optional additional
    methods.
    """

    compontent_meta = dlg_component(
        "MyApp",
        "My Application",
        [dlg_batch_input("binary/*", [])],
        [dlg_batch_output("binary/*", [])],
        [dlg_streaming_input("binary/*")],
    )
    num_trials = dlg_int_param("numtrials", 100)

    def initialize(self, **kwargs):
        self.num_trials = self.parameters.get("numtrials", 100)
        super(MonteCarloDROP, self).initialize(**kwargs)

    def run(self):
        """
        The run method is mandatory for DALiuGE application components.
        """
        pi_estimate = 0.0
        in_points = 0
        for i in range(self.num_trials):
            rand_x = random.random()
            rand_y = random.random()

            distance = math.sqrt(rand_x**2 + rand_y**2)

            if distance <= 1.0:
                in_points += 1

            pi_estimate = 4 * in_points / self.num_trials

        print(self.num_trials)
        print(pi_estimate)

        for output in self.outputs:
            output.write(pickle.dumps(pi_estimate))
