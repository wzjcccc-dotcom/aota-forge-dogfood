import subprocess
import json
import os
import sys
from pathlib import Path

def run_calc(*args):
    root=Path(__file__).parent.parent
    env=os.environ.copy()
    env["PYTHONPATH"]=str(root / "src")+":"+str(root)+":"+env.get("PYTHONPATH","")
    result=subprocess.run([str(root / "calc")] + list(args), capture_output=True, text=True, env=env, cwd=str(root))
    return result

def test_cli_add():
    r=run_calc("add", "1", "2")
    assert r.returncode==0 and r.stdout.strip()=="3"

def test_cli_sub():
    r=run_calc("sub", "5", "3")
    assert r.returncode==0 and r.stdout.strip()=="2"

def test_cli_mul():
    r=run_calc("mul", "4", "6")
    assert r.returncode==0 and r.stdout.strip()=="24"

def test_cli_div():
    r=run_calc("div", "8", "2")
    assert r.returncode==0 and r.stdout.strip()=="4"

def test_cli_json():
    r=run_calc("add", "1", "2", "--json")
    assert r.returncode==0
    data=json.loads(r.stdout.strip())
    assert data["result"]==3

def test_cli_invalid():
    r=run_calc("add", "foo", "2")
    assert r.returncode!=0

def test_cli_div_zero():
    r=run_calc("div", "1", "0")
    assert r.returncode!=0

def test_cli_div_zero_json():
    r=run_calc("div", "1", "0", "--json")
    assert r.returncode!=0
    data=json.loads(r.stdout.strip())
    assert "error" in data
