class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # use Hash Set (since it eliminate duplicates) O(1)time
        # time complexity: O(n*m) m is average size of given email address

        unique = set()
        for e in emails:
            local, domain = e.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "") # erasing every occurrence of .
            unique.add((local, domain))

            # i, local = 0, ""
            # while e[i] not in ["@", "+"]:
            #     if e[i] != ".":
            #         local += e[i]
            #     i += 1
            # while e[i] != "@":
            #     i += 1
            # domain = e[i + 1:] # i+1 until the end of the list
            # unique.add((local, domain))



        return len(unique)
