-- Task7. Average score - creates a stored procedure ComputeAverageScoreForUser.
-- Computes and store the average score for a student.
-- Note: An average score can be a decimal.
DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	UPDATE users
	SET
	average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
	WHERE id = user_id;

END $$

DELIMITER ;
