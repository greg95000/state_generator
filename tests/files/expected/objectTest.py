from testInterface.states.interfaces.objectTestInterface import objectTestInterface


class objectTest:
    def __init__(
        self, object_test: objectTestInterface, testAttribute: int, testAttribute2: str
    ) -> None:
        super().__init__(testAttribute, testAttribute2)
        self._state = object_test

    def transition_to(self, state):
        self._state = state

    def testFunction(self, arg1: int, arg2: str) -> None:
        raise NotImplementedError()

    def testFunction2(self, arg1: int) -> None:
        raise NotImplementedError()
