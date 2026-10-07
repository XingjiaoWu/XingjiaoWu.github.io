---
layout: archive
title: "主要研究工作"
permalink: /research/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<style>
.rd{border:1px solid #dfe8e6;border-radius:6px;background:#fff;padding:1em 1.2em;margin:0 0 1.2em 0}
.rd h3{margin:.1em 0 .3em 0;font-size:1.15em;color:#0e5148}
.rd .rd-tag{display:inline-block;background:#eef3f2;color:#0e5148;border-radius:10px;padding:1px 9px;font-size:.72em;font-weight:600;margin:0 4px 6px 0}
.rd p{font-size:.92em;line-height:1.85;color:#2a3634;margin:.4em 0}
.rd .rd-new{font-size:.85em;color:#0e5148;background:#e9f1ef;border-radius:4px;padding:.6em .9em;margin-top:.6em;line-height:1.8}
.proj{font-size:.88em;line-height:1.9;color:#2a3634}
.proj b{color:#0e5148}
</style>

<div class="rd">
<h3>① 基于情感可控的个性化多模态数字药物生成 <span style="font-size:.6em;color:#b45309">（现阶段重点）</span></h3>
<span class="rd-tag">数字药物</span><span class="rd-tag">AIGC</span><span class="rd-tag">情感计算</span><span class="rd-tag">脑电</span>
<p>在 AIGC（人工智能内容生成）研究中，通过文字控制图像和视频的生成已经达到了较好效果，然而通过人的感受反馈、特别是<b>情感反馈</b>来控制音乐、图像和视频的生成仍是挑战。本研究方向关注能够实时与"个人情感"对齐的多内容（音乐、视频、图像、脑电、文本等）生成技术、鲁棒性的个性化多模态数字内容生成框架，以及基于 HITL 的质量评估与反馈方法，以通过 AIGC 生成能改善情绪的数字内容来缓解焦虑症、抑郁症等精神类疾病。</p>
<p><b>代表性成果</b>：在一区期刊 Information Fusion、IP&amp;M 上提出跨模态情感细粒度对齐与融合方法；在 CCF-B 会议 ICASSP 提出多模态情感交互的多通道注意力图卷积网络；在 McGE'23（CCF-A Workshop）首次提出面向人工设计图像的质量评估方法，获 <b>Best Paper Award</b>；在 ACM MM 2025 提出可控文生乐的时序条件符号对齐方法。</p>
<div class="rd-new">🆕 <b>最新进展（2025–2026）</b>：获批<b>国家自然科学基金青年项目"抑郁症数字疗法关键技术研究"（2025–2028，负责人）</b>；ACL 2026 Findings（APEX，多目标对齐的视觉-语言生成）、ICLR 2026（LVLM 幻觉缓解）相继发表；面向研究生的课程<b>"从 ChatGPT 到心灵疗愈：AI 生成内容与数字药物"</b>与高水平通识课<b>"AI 如何理解我们的情绪"</b>（2025）已开课，形成"科研—课程—转化"闭环。</div>
</div>

<div class="rd">
<h3>② 基于逆强化学习的人在回路计算 <span style="font-size:.6em;color:#b45309">（现阶段重点）</span></h3>
<span class="rd-tag">人在回路 HITL</span><span class="rd-tag">逆强化学习</span><span class="rd-tag">具身智能</span>
<p>依靠挖掘海量数据中的规律解决领域问题已取得显著成效，然而如何用有限数据解决依赖专家知识的领域问题（医学、法律、教育等）仍是难点。本研究关注领域智能体演进过程中关键表征数据的<b>小样本挖掘</b>、具有较强适应性的<b>人机知识融合框架</b>以及高效反馈的人机交互方法，以期构建专家知识介入下可持续演进的领域智能体。</p>
<p><b>代表性成果</b>：在一区期刊提出基于逆强化学习的人在回路方法；在 ICME 提出场景级/对象级双专家蒸馏网络以获取小样本关键表征；在 Knowledge-Based Systems 提出有效聚类算法（K-NNDP）作为支撑；在 ICRA 2025 提出多类型偏好学习方法，赋能基于偏好的强化学习。所提出的人机混合人群计数方法作为核心技术贡献之一，参与获得<b>2022 年度上海市技术发明一等奖</b>（排名 13/15，唯一学生）。</p>
<div class="rd-new">🆕 <b>最新进展（2025–2027 在研）</b>：负责人承担<b>上海市"科技创新行动计划"新一代信息技术关键技术攻关项目"基于人在回路的具身智能学习方法研究"</b>（2025–2027）；参与承担<b>上海市卫生和健康发展研究中心课题"基于人工智能的慢病预测关键技术研究"</b>（2026–2027），将人在回路方法向医疗健康场景落地。</div>
</div>

<div class="rd">
<h3>③ 基于深度学习的复杂文档版面布局分析</h3>
<span class="rd-tag">文档智能</span><span class="rd-tag">版面分析</span><span class="rd-tag">语义排版</span>
<p>简单版面文档理解随大模型发展已逐渐成熟，然而复杂布局文档（杂志、古籍、古代医书）的理解仍是挑战。本研究方向关注复杂版面的<b>生成、挖掘与评估</b>，打通"生成—分析—评估"的完整体系，构建产学研用通路。</p>
<p><b>代表性成果</b>：在 ICME 提出基于图层建模的复杂文档生成方法；在文档处理顶级会议 ICDAR 提出基于 VAE 的文档布局生成框架（LSTMVA）；在 Information Sciences 提出显式边缘嵌入的版面分析方法；在 IP&amp;M 与 ICME 提出动态残差特征融合的统一框架（DRFN）。核心技术获华为认可并开展<b>诺亚方舟实验室合作</b>（2022–2023 子课题负责人），核心指标在 InfographicVQA 任务上居榜首（截至 2023 年 11 月，领先谷歌 17%）；获 CCF 技术公益黑客马拉松最佳方案奖；显式边缘嵌入工作参与获<b>2022 年度上海市科技进步二等奖</b>（排名 6/10）。</p>
<div class="rd-new">🆕 <b>最新进展（2026）</b>：ICML 2026 发表 <b>VecDesigner</b>——面向语义排版（Semantic Typography）的视觉引导与结构一致性生成框架；Knowledge-Based Systems 连续发表证据链驱动检索问答（Evidence-Chain-Driven MQA）与自适应链检索 ACRA 两篇一区论文，研究主线由版面分析延伸至多模态检索增强问答。</div>
</div>

<h2 style="font-size:1.25em;font-weight:700;color:#0e5148;border-bottom:2px solid #0e5148;padding-bottom:4px;margin:1.8em 0 .8em 0">在研项目（负责人）</h2>
<p class="proj">
<b>抑郁症数字疗法关键技术研究</b>　国家自然科学基金青年基金　2025–2028<br>
<b>基于人在回路的具身智能学习方法研究</b>　上海市"科技创新行动计划"新一代信息技术关键技术攻关　2025–2027<br>
<b>AI 情绪演化与类人抑郁性状态研究</b>　华东师大理工科科研"三个十"专项行动计划（原创探索类）　2025–2027<br>
<b>基于人工智能的慢病预测关键技术研究</b>　上海市卫生和健康发展研究中心　2026–2027<br>
<b>"AI 如何理解我们的情绪"课程建设</b>　华东师大研究生高水平通识课建设项目　2025–2027<br>
<b>人工智能技术赋能文化艺术创作</b>　上海市文创办项目　2024–2025（合作方负责人）
</p>
<p class="proj" style="color:#6b7a77;font-size:.82em">已结题：上海市多维度信息处理重点实验室开放课题（2023–2024）；华为诺亚方舟实验室"文档视觉特征统一建模技术"（2022–2023，子课题负责人）；华东师大优秀博士生学术创新能力提升计划（2020–2022）等。</p>

<h2 style="font-size:1.25em;font-weight:700;color:#0e5148;border-bottom:2px solid #0e5148;padding-bottom:4px;margin:1.8em 0 .8em 0">招生信息</h2>
<p class="proj">招收<b>药学</b>（学术学位博导/硕导）、<b>制药工程</b>（专业学位博导/硕导）、<b>应用心理学</b>（专业学位硕导）方向研究生。欢迎具有计算机、药学、心理学交叉背景的同学加入，研究主题围绕 <b>AI4Science、数字药物、人在回路计算</b>。联系邮箱：<b>xjwu@pharm.ecnu.edu.cn</b>。</p>
