class Solution:
    def my_pow_1(self, value: float, power: int) -> float:
        """Naive solution.

        Notes:
            Time Complexity: O(power)
            Space Complexity: O(1)
        """
        return value ** power

    def my_pow_2(self, value: float, power: int) -> float:
        """Use recursive.

        Notes:
            Time Complexity: O(log(power))
            Space Complexity: O(log(power)) (due to stack)
        """
        if power == 0:
            return 1

        if value == 0:
            return 0

        if power < 0:
            value = 1 / value
            power = -power

        half_power, remain = divmod(power, 2)
        half_pow = self.my_pow_2(value, half_power)
        pow_ = half_pow * half_pow
        if remain:
            pow_ *= value
        return pow_

    def my_pow_3(self, value: float, power: int) -> float:
        """Use loop instead of recurisve call.

        Notes:
            Time Complexity: O(log(power))
            Space Complexity: O(1)
        """
        if value == 0:
            return 0

        if power < 0:
            value = 1 / value
            power = -power

        pow_ = 1.0
        while power > 0:
            power, remain = divmod(power, 2)
            pow_ *= (value ** remain)
            value *= value
        return pow_
