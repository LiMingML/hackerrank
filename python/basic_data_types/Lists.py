if __name__ == '__main__':
    N = int(input())
    lst = []
    context = {}
    context["lst"] = lst
    for _ in range(N):
        method_param = input().split()
        code = ""
        method = method_param[0]
        context["method"] = method
        context["method_param"] = method_param
        if method == "print":
            code = "print(lst)"
        if method in {"sort", "pop", "reverse"}:
            code = f"lst.{method}()"
        if method in {"append", "remove"}:
            code = f"lst.{method}(int(method_param[1]))"
        if method == "insert":
            code = f"lst.{method}(int(method_param[1]), int(method_param[2]))"

        exec(code, context)


