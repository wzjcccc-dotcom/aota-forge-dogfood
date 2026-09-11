import subprocess, json, os, sys
from pathlib import Path

def run_calc(*args):
    root = Path(__file__).parent.parent
    env = os.environ.copy()
    env["PYTHONPATH"] = str(root / "src") + ":" + str(root) + ":" + env.get("PYTHONPATH","")
    result = subprocess.run([str(root / "calc")] + list(args), capture_output=True, text=True, env=env, cwd=str(root))
    return result

def test_max_human_2_5():
    r = run_calc("max", "2", "5")
    assert r.returncode == 0
    assert r.stdout.strip() == "5"

def test_max_human_5_2():
    r = run_calc("max", "5", "2")
    assert r.returncode == 0
    assert r.stdout.strip() == "5"

def test_max_json():
    r = run_calc("max", "2", "5", "--json")
    assert r.returncode == 0
    data = json.loads(r.stdout.strip())
    assert data["result"] == 5

def test_max_json_reverse():
    r = run_calc("max", "5", "2", "--json")
    assert r.returncode == 0
    data = json.loads(r.stdout.strip())
    assert data["result"] == 5

def test_max_core():
    from src.calculator.core import max as calc_max
    assert calc_max(2,5) == 5
    assert calc_max(5,2) == 5
    assert calc_max(3,3) == 3
