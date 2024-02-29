                elif d == "R":
                    if i + 1 < len(dom) and dom[i + 1] == ".":
                        # Check for conflicting "L" dominoes
                        if not (i + 2 < len(dom) and dom[i + 2] == "L"):
                            # If no immediate "L" conflict, tip it over
                            dom[i + 1] = "R"
                            q.append((i + 1, "R"))
            