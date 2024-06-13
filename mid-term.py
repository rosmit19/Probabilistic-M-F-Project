# Given probabilities for A, B, C, and D as per the Bayesian network
P_A = {'a0': 0.2, 'a1': 0.8}
P_B_given_A = {'b0a0': 0.5, 'b1a0': 0.5, 'b0a1': 0.2, 'b1a1': 0.8}
P_C_given_B = {'c0b0': 0.5, 'c1b0': 0.5, 'c0b1': 0.2, 'c1b1': 0.8}
P_D_given_B = {'d0b0': 0.9, 'd1b0': 0.1, 'd0b1': 0.3, 'd1b1': 0.7}


# 1(a): Directly from given probabilities
P_A_a1 = P_A['a1']

# 1(b): Compute P(D=d0)
P_B_b0 = P_B_given_A['b0a0'] * P_A['a0'] + P_B_given_A['b0a1'] * P_A['a1']
P_B_b1 = P_B_given_A['b1a0'] * P_A['a0'] + P_B_given_A['b1a1'] * P_A['a1']
P_D_d0 = P_D_given_B['d0b0'] * P_B_b0 + P_D_given_B['d0b1'] * P_B_b1

# 1(c): Compute P(A=a1, B=b0, C=c0, D=d1)
P_A_a1_B_b0_C_c0_D_d1 = P_D_given_B['d1b0'] * P_C_given_B['c0b0'] * P_B_given_A['b0a1'] * P_A['a1']

# 1(d): Compute P(A=a1|B=b0, C=c0, D=d1) using Bayes' theorem and the given data 
P_B_b0_C_c0_D_d1 = P_D_given_B['d1b0'] * P_C_given_B['c0b0'] * P_B_b0
P_A_a1_given_B_b0_C_c0_D_d1 = P_A_a1_B_b0_C_c0_D_d1 / P_B_b0_C_c0_D_d1


# Print results as calculated 
print("P(A=a1) =", P_A_a1)
print("P(D=d0) =", P_D_d0)
print("P(A=a1, B=b0, C=c0, D=d1) =", P_A_a1_B_b0_C_c0_D_d1)
print("P(A=a1|B=b0, C=c0, D=d1) =", P_A_a1_given_B_b0_C_c0_D_d1)


# Code output(Answers):
#a) P(A=a1) = 0.8
#b) P(D=d0) = 0.45600000000000007
#c) P(A=a1, B=b0, C=c0, D=d1) = 0.008000000000000002
#d) P(A=a1|B=b0, C=c0, D=d1) = 0.6153846153846155