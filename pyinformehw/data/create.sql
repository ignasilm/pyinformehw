CREATE VIEW informehw AS
select c.name, u.name as usuario, u.complet_name, c.model,  mp.memorydevices, mem.zocalos_usados,mem.mem_instalada, mem.speed, 
    cpu.name as CPU, CASE WHEN tdd.ssd == 0 THEN 'No' ELSE 'Si' END as ssd, dd.model as HD, 
    dd.size/1000/1000/1000 as capacidad_hd, 
    v.freespace/1000000000 as libre_hd, dd.size/1000/1000/1000 - v.freespace/1000000000 as uso_hd,
    be.fecha, be.core, be.multicore
FROM COMPutersystem c 
left join USER u on u.computer = c.computer
left join MEMPHYSICAL mp on  mp.computer = c.computer
left join CPU cpu on c.computer=cpu.computer 
left join dISKDRIVE dd on c.computer=dd.computer 
left join VOLUME v on c.computer=v.computer 
left join (
	SELECT mc.computer, min(mc.speed) as speed , count(mc.id) as zocalos_usados, sum(mc.capacity)/1024/1024/1024 as mem_instalada
	FROM MEMORYCHIP mc
	group by mc.computer) mem on c.computer=mem.computer 
left join diskmodel tdd on trim(dd.model)=trim(tdd.model)
left join (
    select distinct be_t.computer, be_t.fecha, be_t.core, be_t.multicore
    from (select computer, max(fecha) as ultimo_benchmark 
    from benchmark
    group by computer) ultimo_be
    left join benchmark be_t on be_t.computer = ultimo_be.computer and be_t.fecha = ultimo_be.ultimo_benchmark
) be on be.computer = c.computer
where v.driveletter = 'C:'
    and dd.deviceid = '\\.\PHYSICALDRIVE0'
group by c.name, c.model, c.username, mp.memorydevices,mem.speed
order by tdd.ssd asc, cpu.name asc, mem.mem_instalada asc, mem.speed asc, be.multicore asc, be.core asc;