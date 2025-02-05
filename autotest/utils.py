import numpy as np

print_ans = False


def assert_or_print(
    results,
    answers,
    test_name: str = None,
    print_ans: bool = False,
    close: bool = False,
):
    if test_name is not None:
        test_name = f"{test_name}:"
    n_space = 4
    if print_ans and (test_name is not None):
        print("\n")
        sp = "".join(n_space * [" "])
        n_space = n_space + 2
        print(f"{sp}{test_name}")

    # Always check every test in the answers
    for key in answers.keys():
        if print_ans:
            sp = "".join(n_space * [" "])
            print(f"{sp}{key}: {results[key]}")
        else:
            if close:
                np.testing.assert_allclose(
                    results[key], answers[key], err_msg=f"{test_name}{key}"
                )
            else:
                np.testing.assert_equal(
                    results[key], answers[key], err_msg=f"{test_name}{key}"
                )
            # if isinstance(results[key], (np.datetime64, np.timedelta64)):
            #    assert results[key] == answers[key], msg
            # else:
            #    assert np.isclose(results[key], answers[key]), msg

    # Always fail if printing answers
    assert not print_ans
    return
