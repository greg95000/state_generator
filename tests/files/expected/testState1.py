from testInterface.states.interfaces.statesTestInterface import statesTestInterface
from testInterface.states.models.statesTest import statesTest
from testInterface.states.models.testState2 import testState2
from testInterface.states.models.testState1 import testState1


class testState1State(statesTestInterface):
    def __init__(
        self, states_test: statesTest, testAttributeState1: int, testAttributeState2
    ) -> None:
        super().__init__(states_test, testAttributeState1, testAttributeState2)

    def testFunctionState1(self, arg1: int, arg2: dict) -> None:
        self.states_test.transition_to(
            testState2(self.states_test, testAttributeState1, testAttributeState2)
        )

    def testFunctionState2(self, arg1: str) -> None:
        self.states_test.transition_to(
            testState1(self.states_test, testAttributeState1, testAttributeState2)
        )
