from agents import Agent, Runner

print("Runner dict:", dir(Runner))
import inspect
print("Runner.run signature:", inspect.signature(Runner.run_process)) if hasattr(Runner, 'run_process') else print("No run_process")
if hasattr(Runner, 'run'):
    print("Runner.run signature:", inspect.signature(Runner.run))
