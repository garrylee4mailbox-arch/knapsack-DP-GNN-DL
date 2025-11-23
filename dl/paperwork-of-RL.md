# 1. Introduction to Reinforcement Learning Basics
**Reinforcement Learning (RL)** is one of the three fundamental machine learning paradigms (alongside Supervised Learning and Unsupervised Learning) which especially focuses on how an intelligent agent can take actions in a dynamic and variational environment in order to maximize the cumulative rewards. Unlike Supervised Learning which relies on labeled data, or Unsupervised Learning which seeks patterns in data, RL is concerned with  finding a balance between **exploration** (of undiscovered territory) and **exploitation** (of current knowledge) with the goal of maximizing the cumulative reward (the feedback of action taking). The search for this balance is known as the *Exploration-Exploitation Dilemma*. This section introduces the core components and concepts of Reinforcement Learning, including agents, environments, states, actions, rewards and policies, with explanation of how these elements interact within the **Markov Decision Process (MDP)** framework.
## Core Components & Concepts in RL
Reinforcement Learning focuses on the idea that an agent (the learner or decision-maker) interacts with an environment to finally achieve a goal. The agent make actions and receive feedback to estimate its performance and optimize its decision-making over time. Here are some components:
- **Agent**: The learner or decision-maker that performs actions and interacts with the environment
- **Environment:** The world or system in which the agent interact, provides rewards and feedback in response to agent's actions
- **State (S)**: The situation or condition the agent is currently in. State can be *discrete* (e.g. board positions in chess) or *continuous* (e.g. a robot's position in a space)
- **Action (A):** The possible move or decision the agent could make. Action also can be *discrete* (e.g. left/right) or *continuous* (e.g. steering angles)
- **Reward (R):** The feedback or result from the environment based on the agent's action taken in a state. The reward function is the only feedback the agent receives about its performance.
- **Policy (π):** The agent's strategy, mapping states to actions. Policies can be *deterministic* (always choosing the same action in a state) or *stochastic* (choosing actions according to a probability distribution)
- **Value Function (V(s), Q(s, a)):** Functions estimating the expected cumulative reward from a state (or state-action pair), under a given policy. These are central to many RL algorithm.
### Working of Reinforcement Learning
The agent interacts iteratively with its environment in a feedback loop.

1. The agent observes the current state of the environment.
2. It chooses and performs an action based on its policy.
3. The environment responds by transitioning to a new state and providing a reward or penalty.
4. The agent updates its knowledge (policy, value function) based on the reward received and the new state.
This cycle repeats with the agent balancing **exploration** (trying new actions) and **exploitation** (using known good actions) to maxing the cumulative reward over time.
### Markov Decision Process (MDP) Framework
Most RL problems are formalized as **Markov Decision Processes (MDPs)**, which provide a mathematical structure for sequential decision-making under uncertainty.
A Markov Decision Process is defined by the tuple:
- $S$: is a set of states called the *state space*. The state space can be discrete or continuous like the set of real numbers.
- $A$: is a set of actions called the *action space* (alternatively, $A_s$ is the set of actions available from state $s$). As for the state, actions can be discrete or continuous.
- $P_a(s,s')$: is the transition probability function, providing the probability of moving to the state $s'$ from state $s$ with action $a$ 
- $R_a(s,s')$: is the immediate reward (or expected immediate reward) received after action $a$ is taken to transaction from state $s$ to state $s'$ 
- $\gamma \in [0, 1]$: Discount factor which determines the importance of future rewards relative to immediate rewards. A lower discount factor makes the decision maker more short-sighted.

A particular MDP may have multiple distinct optimal policies. Because of the Markov property, it can be shown that the optimal policy is a function of the current state.
### Policies: Deterministic and Stochastic
A policy $\pi$ defines the agent's behavior. In deterministic policies, $\pi(s)$ yields a specific action for each state. In Stochastic policies, $\pi(as)$ gives the probability of taking action $a$ in state $s$. Stochastic policies are particularly useful in environments with inherent randomness or partial observability, and they facilitate exploration during learning.

The central objective in RL is to find an optimal policy $\pi^*$ , which maximizes the expected cumulative reward (return) from any starting state.
### Value Functions & Bellman Equations
The state-value function $V\pi(s)$ is the expected returen when starting from state $s$ and following policy $\pi$ thereafter:

$$V\pi(s)=E\pi[∑_{k=0}k r_{t+k+1} s_t = s]$$ 

The action-value function $Q\pi(s,a)$ is the expected return from state $s$, taking action a, and then following $\pi$:

$$Q\pi(s,a)=Eπ[∑_{k=0}k r_{t+k+1} s_t = s, a_t = a]$$ 
### Exploration & Exploitation
A fundamental challenge in RL is to balance exploration (trying new actions to discover their effects) and exploitation (choosing actions known to yield high rewards). Strategies such as $\epsilon$ - greedy (choosing a random action with probability $\epsilon$, otherwise the best-known action) are commonly used to manage this trade-off.
### Categories of RL Algorithm
RL algorithm can be broadly categorized as:
- Value-based methods: Learn value functions (e.g. Q-learning, SARSA) and derive policies from them.
- Policy-based methods: Directly optimize the policy.
- Actor-Critic methods: Combine value-based and policy-based approaches, with an actor (policy) and a critic (value function).
Recent advances in Deep Reinforcement Learning (DRL) integrate deep neural networks as function approximators, enabling RL to tackle high-dimensional and complex environments.

## Modeling the Knapsack Problem with Reinforcement Learning
The Knapsack Problem (KP) is a classic combinatorial optimization problem, widely studied due to its theoretical significance and practical applications in logistics, finance and resource allocation. In its 0-1 variant, the problem is to select a subset of items, each with a value and weight, to maximize total value without exceeding the knapsack's capacity.
### The Definition of 0/1 Knapsack Problem
Given $n$ items where each item has some weight and profit associated with it and also given a bag with capacity $W$(i.e. the bag can hold at most $W$ weight in it). The task is to put the items into the bag such that the sum of profits associated with them is the maximum possible.

**Note:** The constraint here is we can either put an item completely into the bag or cannot put it at all (It is not possible to put a part of an item into the bag).

> [Here is an example]
> **Input:** W = 4, **profit**[ ] = [1, 2, 3], **weight**[ ] = [4, 5, 1]
> **Output:** 3
> **Explanation:** There are two items which have weight less than or equal to 4. If we selec the item with weight 4, the possible value is 1. And if we select the item with weight 1, the possible value is 3. So the maximum possible profit is 3. Note that we cannot put both the items with weight 4 and 1 together as the capacity of the bag is 4.

### Formulating the Knapsack Problem as an MDP
To apply Reinforcement Learning (RL), the Knapsack Problem (KP) must be cast as an Markov Decision Process (MDP). This involves defining the state space, action space, transition dynamics, and reward function.

**State Representation**
The state should encapsulate all information necessary for decision-making. Common representations include:

- **Binary vector:** Each element indicates whether an item is included or not. 
- **Tuple:** (current total weight, current total value, items selected so for).
- **Aggregated features:** For large instances, state aggregation or embedding techniques can reduce dimensionality and improve scalability.

**Action Representation**
At each step, the agent decides which item to include next (or to skip). Actions can be:
Discrete: Select item $j$ (if not already chosen and if feasible), or skip.
Masking: Actions corresponding to infeasible or already-selected items are masked out to prevent illegal moves.

**Transition Dynamics**
The environment transitions deterministically: selecting an item updates the state by marking the item as chosen and updating the total weight and value. If the capacity is exceeded, the episode may terminate or a penalty may be implemented.

Example Reward Function
A typical reward function for the KP might be:
- $+v_j$ if item $j$ is added and the solution remains feasible
- $-w_j$ if adding item $j$ exceeds capacity
- $-W$ if an illegal action is taken (e.g. select an already-chosen item)
- Final reward: total value if feasible, large penalty if not.
