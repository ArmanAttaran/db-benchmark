#!/usr/bin/env python

print("# join-pydatatable.py", flush=True)

import os
import gc
import timeit
import copy
import datatable as dt
from datatable import f, sum, join, isna
from datatable.math import isfinite

exec(open("./helpers.py").read())

ver = dt.__version__
git = dt.__git_revision__
task = "join"
solution = "pydatatable"
fun = "join"
cache = "TRUE"

data_name = os.environ['SRC_JN_LOCAL']
on_disk = data_name.split("_")[1] == "1e9" ## for 1e9 join use on-disk data table
fext = "jay" if on_disk else "csv"
src_jn_x = os.path.join("data", data_name+"."+fext)
y_data_name = join_to_tbls(data_name)
src_jn_y = [os.path.join("data", y_data_name[0]+"."+fext), os.path.join("data", y_data_name[1]+"."+fext), os.path.join("data", y_data_name[2]+"."+fext)]
if len(src_jn_y) != 3:
    raise Exception("Something went wrong in preparing files used for join")

print("loading datasets " + data_name + ", " + y_data_name[0] + ", " + y_data_name[2] + ", " + y_data_name[2], flush=True)

if on_disk:
    x = dt.open(src_jn_x)
    small = dt.open(src_jn_y[0])
    medium = dt.open(src_jn_y[1])
    big = dt.open(src_jn_y[2])
else:
    x = dt.fread(src_jn_x)
    small = dt.fread(src_jn_y[0])
    medium = dt.fread(src_jn_y[1])
    big = dt.fread(src_jn_y[2])

print(x.nrows, flush=True)
print(small.nrows, flush=True)
print(medium.nrows, flush=True)
print(big.nrows, flush=True)

print("joining...", flush=True)

question = "small inner on int" # q1
gc.collect()
y = copy.deepcopy(small)
t_start = timeit.default_timer()
y.key = 'id1'
ans = x[:, :, join(y)][isfinite(f.v2), :] # , on='id1'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans, y
gc.collect()
y = copy.deepcopy(small)
t_start = timeit.default_timer()
y.key = 'id1'
ans = x[:, :, join(y)][isfinite(f.v2), :] # , on='id1'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans, y

question = "medium inner on int" # q2
gc.collect()
y = copy.deepcopy(medium)
t_start = timeit.default_timer()
y.key = 'id2'
ans = x[:, :, join(y)][isfinite(f.v2), :] # , on='id2'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans, y
gc.collect()
y = copy.deepcopy(medium)
t_start = timeit.default_timer()
y.key = 'id2'
ans = x[:, :, join(y)][isfinite(f.v2), :] # , on='id2'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans, y

question = "medium outer on int" # q3
gc.collect()
y = copy.deepcopy(medium)
t_start = timeit.default_timer()
y.key = 'id2'
ans = x[:, :, join(y)] # , on='id2', how='left'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans, y
gc.collect()
y = copy.deepcopy(medium)
t_start = timeit.default_timer()
y.key = 'id2'
ans = x[:, :, join(y)] # , on='id2', how='left'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans, y

question = "medium inner on factor" # q4
gc.collect()
y = copy.deepcopy(medium)
t_start = timeit.default_timer()
y.key = 'id5'
ans = x[:, :, join(y)][isfinite(f.v2), :] # , on='id5'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans, y
gc.collect()
y = copy.deepcopy(medium)
t_start = timeit.default_timer()
y.key = 'id5'
ans = x[:, :, join(y)][isfinite(f.v2), :] # , on='id5'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans, y

question = "big inner on int" # q5
gc.collect()
y = copy.deepcopy(big)
t_start = timeit.default_timer()
y.key = 'id3'
ans = x[:, :, join(y)][isfinite(f.v2), :] # , on='id3'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=1, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
del ans, y
gc.collect()
y = copy.deepcopy(big)
t_start = timeit.default_timer()
y.key = 'id3'
ans = x[:, :, join(y)][isfinite(f.v2), :] # , on='id3'
print(ans.shape, flush=True)
t = timeit.default_timer() - t_start
m = memory_usage()
t_start = timeit.default_timer()
chk = ans[:, [sum(f.v1), sum(f.v2)]]
chkt = timeit.default_timer() - t_start
write_log(task=task, data=data_name, in_rows=x.shape[0], question=question, out_rows=ans.shape[0], out_cols=ans.shape[1], solution=solution, version=ver, git=git, fun=fun, run=2, time_sec=t, mem_gb=m, cache=cache, chk=make_chk(flatten(chk.to_list())), chk_time_sec=chkt)
print(ans.head(3).to_pandas(), flush=True)
print(ans.tail(3).to_pandas(), flush=True)
del ans, y

exit(0)
