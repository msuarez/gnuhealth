-- Update tax line sign
UPDATE account_tax_line SET amount = -amount WHERE id IN (SELECT tl.id FROM  account_tax_line AS tl JOIN account_move_line AS ml ON tl.move_line = ml.id JOIN account_move AS m ON ml.move = m.id JOIN account_invoice AS i ON i.id = CAST(SUBSTRING(m.origin, 17) AS INTEGER) AND m.origin like 'account.invoice,%' WHERE tl.amount > 0 AND ml.credit > 0 AND i.type = 'in');

UPDATE account_tax_line SET amount = -amount WHERE id IN (SELECT tl.id FROM  account_tax_line AS tl JOIN account_move_line AS ml ON tl.move_line = ml.id JOIN account_move AS m ON ml.move = m.id JOIN account_invoice AS i ON i.id = CAST(SUBSTRING(m.origin, 17) AS INTEGER) AND m.origin like 'account.invoice,%' WHERE tl.amount > 0 AND ml.debit > 0 AND i.type = 'out');

-- Update tax lines of inactive tax to their parent 
UPDATE account_tax_line as l SET tax = (SELECT parent FROM account_tax WHERE account_tax.id = tax) FROM account_tax as t WHERE l.tax = t.id AND t.active = false;

-- Delete duplicate tax lines (run multiple times until no record are deleted)
DELETE FROM account_tax_line WHERE id IN (SELECT MAX(id) FROM account_tax_line GROUP BY tax, amount, type, move_line HAVING count(*) > 1);
