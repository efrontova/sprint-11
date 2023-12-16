-- Задание 1 --  вывести список логинов курьеров с количеством их заказов в статусе «В доставке».
SELECT c.login, COUNT(o.id) FROM "Couriers" AS c LEFT JOIN "Orders" AS o ON c.id = o."courierId" AND o."inDelivery" = true GROUP BY c.login;

-- Задание 2 -- вывести все трекеры заказов и их статусы.
SELECT track, CASE WHEN finished = true then '2' WHEN cancelled = true then '-1' WHEN "inDelivery"=true then '1' ELSE '0' END AS status FROM "Orders" LIMIT 10;
