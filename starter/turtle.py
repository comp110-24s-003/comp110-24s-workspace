"""Support code for the Turtle Graphics template interop."""

from pydantic import BaseModel


class AmountCommand(BaseModel):
    type: str
    amount: float


class CoordinateCommand(BaseModel):
    type: str
    x: float
    y: float


class Turtle(BaseModel):

    commands: list[AmountCommand | CoordinateCommand] = []

    def forward(self, amount: float) -> None:
        self.commands.append(AmountCommand(type="forward", amount=amount))

    def backward(self, amount: float) -> None:
        self.commands.append(AmountCommand(type="backward", amount=amount))

    def left(self, angle: float) -> None:
        self.commands.append(AmountCommand(type="left", amount=angle))

    def right(self, angle: float) -> None:
        self.commands.append(AmountCommand(type="right", amount=angle))

    def turnTo(self, angle: float) -> None:
        self.commands.append(AmountCommand(type="turnTo", amount=angle))

    def setSpeed(self, speed: float) -> None:
        self.commands.append(AmountCommand(type="setSpeed", amount=speed))

    def moveTo(self, x: float, y: float) -> None:
        self.commands.append(CoordinateCommand(type="moveTo", x=x, y=y))
