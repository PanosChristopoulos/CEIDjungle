USE erecruit;

mysql> DELIMITER $$ ;

CREATE PROCEDURE candidate_rank_list(IN jobid int(4))
BEGIN
DECLARE username VARCHAR (12);
DECLARE fullscore TINYINT;
DECLARE personality TINYINT;
DECLARE education TINYINT;
DECLARE experience TINYINT;
DECLARE rejection_reason TEXT DEFAULT  " ";
SELECT personality_score, education_score, experience_score INTO personality, education, experience FROM interviews
WHERE interview_job = jobid AND cand_name = username;
IF personality = 0 THEN 
SET rejection_reason = CONCAT(rejection_reason,"Failed the interview");
END IF;
IF education = 0 THEN
SET rejection_reason = CONCAT(rejection_reason, "Inadequate Education");
END IF;
IF experience = 0 THEN
SET rejection_reason = CONCAT(rejection_reason, "No prior experience");
END IF;
SELECT cand_usrname, (interviews.personality_score + interviews.education_score + interviews.experience_score) AS fullscore
FROM applies
INNER JOIN interviews ON 
(applies.job_id = jobid AND applies.job_id = interviews.interview_job AND applies.cand_usrname = interviews.cand_name)
GROUP BY cand_usrname 
ORDER BY (AVG(interviews.personality)+SUM(interviews.education)+SUM(interviews.experience)) DESC;
END

DELIMITER //
CREATE TRIGGER candidate_insert AFTER INSERT ON candidate
FOR EACH ROW
BEGIN 
INSERT INTO Logging VALUES (NULL, username ,NOW(), 'Y','Insert', 'candidate');
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER candidate_delete AFTER DELETE ON candidate
FOR EACH ROW
BEGIN 
INSERT INTO Logging VALUES (NULL, username ,NOW(), 'Y','Delete', 'candidate');
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER candidate_update AFTER UPDATE ON candidate
FOR EACH ROW
BEGIN 
INSERT INTO Logging VALUES (NULL, username ,NOW(), 'Y','Update', 'candidate');
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER recruiter_insert AFTER INSERT ON recruiter
FOR EACH ROW
BEGIN 
INSERT INTO Logging VALUES (NULL, username ,NOW(), 'Y','Insert', 'recruiter');
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER recruiter_delete AFTER DELETE ON recruiter
FOR EACH ROW
BEGIN 
INSERT INTO Logging VALUES (NULL, username ,NOW(), 'Y','Delete', 'recruiter');
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER recruiter_update AFTER UPDATE ON recruiter
FOR EACH ROW
BEGIN 
INSERT INTO Logging VALUES (NULL, username ,NOW(), 'Y','Update', 'recruiter');
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER job_insert AFTER INSERT ON job
FOR EACH ROW
BEGIN 
INSERT INTO Logging VALUES (NULL, username ,NOW(), 'Y','Insert', 'job');
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER job_delete AFTER DELETE ON job
FOR EACH ROW
BEGIN 
INSERT INTO Logging VALUES (NULL, username ,NOW(), 'Y','Delete', 'job');
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER job_update AFTER UPDATE ON job
FOR EACH ROW
BEGIN 
INSERT INTO Logging VALUES (NULL, username ,NOW(), 'Y','Update', 'job');
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER etaireia_insert AFTER INSERT ON etaireia
FOR EACH ROW
BEGIN 
INSERT INTO Logging VALUES (NULL, username ,NOW(), 'Y','Insert', 'etaireia');
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER etaireia_delete AFTER DELETE ON etaireia
FOR EACH ROW
BEGIN 
INSERT INTO Logging VALUES (NULL, username ,NOW(), 'Y','Delete', 'etaireia');
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER etaireia_update AFTER UPDATE ON etaireia
FOR EACH ROW
BEGIN 
INSERT INTO Logging VALUES (NULL, username ,NOW(), 'Y','Update', 'etaireia');
END //
DELIMITER ;

DELIMITER //
CREATE TRIGGER prevent_delete AFTER DELETE ON applies
FOR EACH ROW
BEGIN
IF( SELECT submission_date FROM job WHERE job_id = job.id) <NOW() THEN
SET @s = 'SUBMISSION DUE DATE HAS PASSED. NO APPLICATION CAN BE DELETED!';
SET MESSAGE_TEXT = @s;
END IF;
END//