%Train a Naive Bayes Classifier with 5 fold cross validation
predictorNames = {'Pregnancies','Glucose','BloodPressure', 'SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome'};
%load the attributes on a table
NormalTable = DataTable3(:,predictorNames);
%response table used to separate classes 1,2
response = DataTable3{:,10};

gamma = 0:20;
c = 0;
gamma = gamma * 0.5;
max = 0;
max2 = 0;



for j = 1:5:200
    svmModel = fitcsvm(NormalTable,response,...
    'KernelFunction','LINEAR','BoxConstraint',j);
    crossmodel = crossval(svmModel, 'KFold', 5);
    ActualLabel = crossmodel.Y;
    PredictedLabel = resubPredict(svmModel);
    performance = classperf(ActualLabel,PredictedLabel);
    s = performance.Specificity;
    sens = performance.Sensitivity;
    gm = sqrt(s*sens);
    CorrectRate = performance.CorrectRate;
    ErrorRate = performance.ErrorRate;
    if (max2 < gm) 
        max2 = gm;
        c = j;
    end
    fprintf('Value C = %f Performance = %f \n',j,gm);
end

for i = gamma
svmModel =fitcsvm(NormalTable,response,'KernelFunction','rbf','KernelScale', 1/sqrt(i),'BoxConstraint', 1);
    crossmodel = crossval(svmModel, 'KFold', 5);
    ActualLabel = crossmodel.Y;
    PredictedLabel = resubPredict(svmModel);
    performance = classperf(ActualLabel,PredictedLabel);
    s = performance.Specificity;
    sens = performance.Sensitivity;
    gm = sqrt(s*sens);
    if (max < gm) 
        max = gm;
        Gamma = i;
    end
    fprintf('Value C = %d ,Value gamma = %f Performance = %f \n',c,i,gm);
end

fprintf('Best Gamma = %f with a performance of %f ',Gamma,max);

