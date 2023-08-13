# Running the analysis with Snakemake

``` bash
snakemake --cluster "sbatch -A {cluster.account} -q {cluster.qos} -c {cluster.cpus-per-task} -N {cluster.Nodes}  -t {cluster.runtime} --mem {cluster.mem} -J {cluster.jobname} --mail-type={cluster.mail_type} --mail-user={cluster.mail} --output {cluster.out} --error {cluster.err}" --cluster-config cluster.json --jobs 100 --latency-wait 120 --configfile run_experiment.json
```
