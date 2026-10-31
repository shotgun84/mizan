import glob,statistics as st,os
CT=51.67
fs=sorted(glob.glob("postProcessing/sets/*/*_C.xy")+glob.glob("postProcessing/sampleDict/*"))
if not fs: fs=sorted(glob.glob("postProcessing/**/*.xy",recursive=True))
print("plane Cbar sigma CoV MI merr%")
for f in fs:
    try: v=[float(l.split()[-1]) for l in open(f) if l.strip() and len(l.split())>=2]
    except: continue
    if not v: continue
    m=st.mean(v);s=st.pstdev(v) if len(v)>1 else 0.0
    cov=s/m if m else 0;mi=max(0,1-cov);me=100*(m-CT)/CT
    print(f"{os.path.basename(f)} {m:.3f} {s:.3f} {cov:.4f} {mi:.4f} {me:+.2f}%")
