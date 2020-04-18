#
#     Kwola is an AI algorithm that learns how to use other programs
#     automatically so that it can find bugs in them.
#
#     Copyright (C) 2020 Kwola Software Testing Inc.
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as
#     published by the Free Software Foundation, either version 3 of the
#     License, or (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import unittest

def main():
    """
        This is the entry point for the Kwola secondary command, kwola_train_agent.

        It is basically identical in behaviour as the main function.
    """
    suite = unittest.defaultTestLoader.loadTestsFromName("kwola.tests.test_training_loop.TestTrainingLoop")
    suite = unittest.defaultTestLoader.loadTestsFromName("kwola.tests.test_end_to_end.TestEndToEnd")

    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)
