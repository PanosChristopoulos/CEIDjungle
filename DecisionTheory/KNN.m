%Train a Naive Bayes Classifier with 5 fold cross validation
predictorNames = {'Pregnancies','Glucose','BloodPressure', 'SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome'};
%load the attributes on a table
NormalTable = DataTable3(:,predictorNames);
%response table used to separate classes 1,2
response = DataTable3{:,10};

max = 0;
k = 3:10;
K = 3;
for i = k
    KnnModel = fitcknn(NormalTable, response, 'NumNeighbors', i);
    CrossModel = crossval(KnnModel,'KFold', 5);
    ActualLabel = CrossModel.Y;
    PredictedLabel = resubPredict(KnnModel);
    
    Performance = classperf(ActualLabel,PredictedLabel);
    Specificity = Performance.Specificity;
    Sensitivity = Performance.Sensitivity;
    
    GeometricMean = sqrt(Sensitivity * Specificity);
    
    if(max < GeometricMean)
        max = GeometricMean;
        K = i;
    end
    
    fprintf('K = %d, performance = %f\n', i, GeometricMean);
end

fprintf('Best K = %d, With performance = %f\n', K, max);
