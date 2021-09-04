class interfaceTestInterface:
    def __init__(
        self,
        testAttributeState1: int,
        testAttributeState2
    ) -> None:
        self.testAttributeState1 = testAttributeState1
        self.testAttributeState2 = testAttributeState2

    def testFunctionState1(
        self,
        arg1: int,
        arg2: dict
    ) -> None:
        raise NotImplementedError()
    
    def testFunctionState2(
        self,
        arg1: str
    ) -> None:
        raise NotImplementedError()
    