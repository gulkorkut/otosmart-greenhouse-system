package com.nht.activitytrackerserver.service;

import com.nht.activitytrackerserver.model.PredictionResult;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class PredictionService {

    private final String FASTAPI_URL = "http://localhost:9000/predict";

    public PredictionResult getPrediction(byte[] imageData) {
        // FastAPI'ye resmi gönder
        String predictionUrl = FASTAPI_URL;
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_OCTET_STREAM);
        HttpEntity<byte[]> requestEntity = new HttpEntity<>(imageData, headers);

        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<PredictionResult> responseEntity = restTemplate.exchange(
                predictionUrl,
                HttpMethod.POST,
                requestEntity,
                PredictionResult.class
        );

        // FastAPI'den gelen sonucu al

        // Sonucu istemciye gönder
        // Burada istediğiniz işlemleri gerçekleştirebilirsiniz, örneğin DTO'yu oluşturabilir ve geri döndürebilirsiniz.
        return responseEntity.getBody();
    }
}

