if len(nums) % 2 != 0:
                    return False

                counts = {}
                for num in nums:
                    if num in counts:
                        counts[num] += 1
                    else:
                        counts[num] = 1

                for count in counts.values():
                    if count % 2 != 0:
                        return False

                return True
