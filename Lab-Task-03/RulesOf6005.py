class RulesOf6005:
    @staticmethod
    def may_use_code_in_assignment(written_by_yourself, available_to_others,
                                   written_as_coursework, citing_your_source,
                                   implementation_required):
        if written_by_yourself:
            return True
        if not written_by_yourself:
            return available_to_others and implementation_required
        return False




# INTENTIONALLY FLAWED CODE
# class RulesOf6005:
#     @staticmethod
#     def may_use_code_in_assignment(written_by_yourself, available_to_others,
#                                     written_as_course_work, citing_your_source,
#                                     implementation_required):
#         # Intentionally incorrect logic for testing
#         return False  # Always returns False, breaking the conditions

# if __name__ == "__main__":
#     # Test cases
#     print("You may certainly use code you wrote yourself: " +
#           str(RulesOf6005.may_use_code_in_assignment(True, False, True, True, True)))