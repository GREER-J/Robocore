# from src.state import State
# import numpy as np

# def test_state_to_array_is_correct_size():
#     nx = 5
#     nu = 2
#     k = 1.23
#     M = 2.1342
#     A = np.array([[-k, k], [k, -k]])
#     B = np.array([[1/M], [1/M]])
#     f = lambda x, u: A @ x + B @ u
#     state = State(nx, nu, f)
#     x = state.mu
#     assert x.shape == (nx, 1), f"Expected shape {(nx, 1)}, but got {x.shape}"

# def test_state_predicts_to_correct_time():
#     nx = 5
#     nu = 2
#     f = lambda x, u: np.eye(nx) @ x
#     state = State(nx, nu, f)

#     t = 0.2
#     state.predict(t)
#     assert state.time == t, f"Expected time of {t}, but got {state.time}"

# def test_state_does_update_on_predict():
#     nx = 2
#     nu = 2
#     k = 1.23
#     M = 2.1342
#     A = np.array([[-k, k], [k, -k]])
#     B = np.array([[1/M], [1/M]])
#     f = lambda x, u: A @ x + B @ u
#     state = State(nx, nu, f)
#     x0 = state.mu.copy()  # Make a copy to compare post-prediction
#     state.predict(2.3)
#     assert np.all(state.mu == x0 + 2.3 * f(x0, state._u)), "State didn't update as expected!"
